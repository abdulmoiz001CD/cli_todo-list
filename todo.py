import click
import os
import json

TODO_FILE = "todo.json"

def load_todo():
    if os.path.exists(TODO_FILE):
     with open(TODO_FILE,"r") as file:
        return json.load(file)
    else:
        return[]

def save_todo(tasks):
    with open(TODO_FILE,"w") as file:
        json.dump(tasks,file,indent=4)

@click.group()
def cli():
    """Todo list manager"""
    pass

@click.command()
@click.argument("task")
def add(task):
    """Add a new task to the list"""
    tasks = load_todo()
    tasks.append({"task":task, "done":False})
    save_todo(tasks)
    click.echo(f"Task {tasks} successfully added")

@click.command()
def list():
    """List all Tasks"""
    tasks = load_todo()
    if not tasks:
        click.echo("No Task found")
        return
    for index, task in enumerate(tasks,1):
        status = "done" if task['done'] else 'pending'
        click.echo(f"{index}.{task['task']} {status}")
    

@click.command()
@click.argument("task_number", type=int)
def complete(task_number):
    """Mark the Task complete"""
    tasks = load_todo()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"]= True 
        save_todo(tasks)
        click.echo(f"Task {task_number} marked as completed")

    else:
        click.echo(f"Invalide task number {task_number}")
 


@click.command()
@click.argument("task_number",type=int)
def delete(task_number):
    """Delete the Task"""
    tasks= load_todo()
    if 0 < task_number <= len(tasks):
        delete_task = tasks.pop(task_number - 1)
        save_todo(delete_task)
        click.echo(f"Task {delete_task['task']} deleted")

    else:
        click.echo(f"Invalide task number {task_number}")





cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(delete)

if __name__ == "__main__":
    cli()
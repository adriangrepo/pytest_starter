#!/usr/bin/env python3

"""
This module is used to create calculation functions including addition, subtraction, multiplication, and division.
This module will also be invoked as a command line script using click
"""

import click

def add(a, b):
    """
    This function is used to add two numbers.
    """
    return a + b

def subtract(a, b):
    """
    This function is used to subtract two numbers.
    """
    return a - b

#build a click group
@click.group()
def cli():
    """
    This is a calculator app
    """

#build a click command
@cli.command("add")
@click.argument("a", type=int)
@click.argument("b", type=int)
def add_command(a, b):
    """
    This command is used to add two numbers.
    """
    #invoke the add function with colored output from click
    click.echo(click.style(str(add(a, b)), fg="green"))

#build a click command
@cli.command("subtract")
@click.argument("a", type=int)
@click.argument("b", type=int)
def subtract_command(a, b):
    """
    This command is used to subtract two numbers.
    """
    #invoke the subtract function with colored output from click
    click.echo(click.style(str(subtract(a, b)), fg="red"))

if __name__ == "__main__":
    cli()   



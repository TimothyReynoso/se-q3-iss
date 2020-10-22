#!/usr/bin/env python

__author__ = 'Timothy Reynoso'

import requests
import json
import turtle
import time


def list_of_the_astronauts():
    iss_data = requests.get('http://api.open-notify.org/astros.json')
    iss_crew_str = iss_data.text
    iss_crew_dict = json.loads(iss_crew_str)
    print('\nNumber of astronauts in Space: ', iss_crew_dict["number"], '\n')
    print('Current astronauts in Space: \n')
    for astro in iss_crew_dict["people"]:
        print('Crew Member Name: ', astro['name'])
        print('Spacecraft:', astro['craft'], '\n')
    return


def iss_location():
    iss_location_data = requests.get(
        'http://api.open-notify.org/iss-now.json')
    return json.loads(iss_location_data.text)


def iss_over_indianapolis():
    payload = {'lat': '39.7684', 'lon': '86.1581'}
    iss_over_indianapolis_data = requests.get(
        'http://api.open-notify.org/iss-pass.json', params=payload)
    return json.loads(iss_over_indianapolis_data.text)


def turtle_graphics():
    screen = turtle.Screen()
    screen.register_shape('iss.gif')
    screen.bgpic('map.gif')
    turtle.setup(720, 360)
    turtle.setworldcoordinates(-180, -90, 180, 90)

    iss_passover_indi = iss_over_indianapolis()
    iss_pass_indi_time = time.ctime(
        iss_passover_indi['response'][0]['risetime'])

    iss_indianapolis = turtle.Turtle()
    iss_indianapolis.color('yellow')
    iss_indianapolis.penup()
    iss_indianapolis.shapesize(0.5, 0.5, 0.5)
    iss_indianapolis.shape('circle')
    iss_indianapolis.goto(-86.158056, 39.768611)
    iss_indianapolis.write(f'{iss_pass_indi_time}', False)

    iss_loc = iss_location()

    _iss = turtle.Turtle()

    _iss.color('red')
    _iss.pensize(5)
    _iss.penup()
    _iss.shape('iss.gif')

    lat_long = iss_loc['iss_position']

    _iss.goto(float(lat_long['longitude']), float(lat_long['latitude']))

    turtle.done()
    pass


def main():
    # iss_over_indianapolis()
    list_of_the_astronauts()
    # iss_location()
    turtle_graphics()
    pass

if __name__ == '__main__':
    main()

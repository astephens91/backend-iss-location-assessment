#!/usr/bin/env python

__author__ = 'astephens91 (collaborated with ZacharyKline on Turtle function)'

import requests
import json
import time
import turtle

# http://api.open-notify.org/astros.json
# http://api.open-notify.org/iss-now.json


def get_crew():
    """Gets list of crew members on ISS and prints them"""
    crew = requests.get('http://api.open-notify.org/astros.json')
    crew_dict = crew.text
    crew_dict = json.loads(crew_dict)
    for crew_member in crew_dict['people']:
        print('{} is on the ISS, just floating in space'
              .format(crew_member['name']))


def get_coords():
    """Gets long/lat coordinates of ISS and prints them"""
    coords = requests.get('http://api.open-notify.org/iss-now.json')
    coords_dict = coords.text
    coords_dict = json.loads(coords_dict)
    longitude = coords_dict['iss_position']['longitude']
    latitude = coords_dict['iss_position']['latitude']
    print(
      "The ISS is currectly floating in space at {} longitude and {} latitude"
      .format(longitude,
              latitude))
    return(float(longitude),
           float(latitude))


def time_until_pass():
    timestamp = requests.get('http://api.open-notify.org/iss-pass.json',
                             {'lon': -86.1349, 'lat': 39.7684, 'n': 1})
    timestamp_dict = timestamp.text
    timestamp_dict = json.loads(timestamp_dict)
    for times in timestamp_dict['response']:
        next_pass = time.ctime(times['risetime'])
    print("The ISS will next be above Indianapolis, IN {}".format(next_pass))
    return "The ISS will next be above Indianapolis, IN {}".format(next_pass)


def create_map(pos):
    new_screen = turtle.Screen()
    new_screen.bgpic('./map.gif')
    new_screen.addshape('iss.gif')
    new_screen.setup(width=720, height=360)
    new_screen.setworldcoordinates(-180, -90, 180, 90)
    new_var = turtle.Turtle()
    new_var.penup()
    new_var.goto(pos)
    indy_cords = turtle.Turtle()
    indy_cords.shape('circle')
    indy_cords.color('purple')
    indy_cords.penup()
    indy_cords.goto(-86.1349, 39.7684)
    timestamp = turtle.Turtle()
    timestamp.color('red')
    timestamp.penup()
    timestamp.goto(-86.1349, 39.7684)
    timestamp.write(time_until_pass(), font=("Arial", 14, "normal"))
    new_screen.exitonclick()


def main():
    get_crew()
    coordinates = get_coords()
    create_map(coordinates)
    time_until_pass()


if __name__ == '__main__':
    main()

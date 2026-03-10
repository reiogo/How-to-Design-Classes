from dataclasses import dataclass
from typing import Protocol
import math

class IGalleryItem(Protocol):
    # computes how long it takes to download a file given a network connection speed
    # in bytes per second
    def timeToDownload(self, bps:int) -> int:
        ...
    # determines whether the file is smaller than some given maximum size
    def smallerThan(self, maxSize:int) -> bool:
        ...
    # determines whether this name is the same as that name
    def sameName(self,thatName:str) -> bool:
        ...

class Image:
    name:str
    size:int #bytes
    height:int #pixels
    width:int #pixels
    quality:str

    def __init__(self, name:str, size:int,  height:int,  width:int,  quality:str):
        self.name = name
        self.size = size
        self.height = height
        self.width = width
        self.quality = quality

    # computes how long it takes to download a file given a network connection speed
    # in bytes per second
    def timeToDownload(self, bps:int) -> int:
        #self.size 
        return self.size//bps
    # determines whether the file is smaller than some given maximum size
    def smallerThan(self, maxSize:int) -> bool:
        return self.size < maxSize
    # determines whether this name is the same as that name
    def sameName(self,thatName:str) -> bool:
        return self.name == thatName

class Text:
    name:str
    size:int #bytes
    numLines:int
    def __init__(self, name:str, size:int, numLines:int):
        self.name = name
        self.size = size
        self.numLines = numLines

    # computes how long it takes to download a file given a network connection speed
    # in bytes per second
    def timeToDownload(self, bps:int) -> int:
        return self.size // bps
    # determines whether the file is smaller than some given maximum size
    def smallerThan(self, maxSize:int) -> bool:
        return self.size < maxSize
    # determines whether this name is the same as that name
    def sameName(self,thatName:str) -> bool:
        return self.name == thatName

class Mp3:
    name:str
    size:int #bytes
    playing_time:int #second
    def __init__(self, name:str, size:int, playing_time:int):
        self.name = name
        self.size = size
        self.playing_time = playing_time

    # computes how long it takes to download a file given a network connection speed
    # in bytes per second
    def timeToDownload(self, bps:int) -> int:
        return self.size // bps

    # determines whether the file is smaller than some given maximum size
    def smallerThan(self, maxSize:int) -> bool:
        return self.size < maxSize

    # determines whether this name is the same as that name
    def sameName(self,thatName:str) -> bool:
        return self.name == thatName

# Grocery Store ==================================================

# an interface for grocery items
class GroceryItem(Protocol):
    # computes unit price (cents per gram)
    def unitPrice(self) -> float:
        ...

    #determines whether unit price is lower than a given amount
    def lowerUnitPrice(self) -> bool:
        ...

    # determines whether a grocery items's unit price is less than
    # that item's unit price
    def cheaperThan(self, that:GroceryItem) -> bool:
        ...

# implements GroceryItem
@dataclass
class IceCream:
    name:str
    weight:int #grams
    price:int #cents
    flavor:str

    # computes unit price (cents per gram)
    def unitPrice(self) -> float:
        return self.price / self.weight

    #determines whether unit price is lower than a given amount
    def lowerUnitPrice(self, thatPrice) -> bool:
        return self.unitPrice() < thatPrice

    # determines whether a grocery items's unit price is less than
    # that item's unit price
    def cheaperThan(self, that:GroceryItem) -> bool:
        return self.unitPrice() < that.unitPrice()

# implements GroceryItem
@dataclass
class Coffee:
    name:str
    weight:int #grams
    price:int #cents
    decaf:bool

    # computes unit price (cents per gram)
    def unitPrice(self) -> float:
        return self.price / self.weight

    #determines whether unit price is lower than a given amount
    def lowerUnitPrice(self, thatPrice) -> bool:
        return self.unitPrice() < thatPrice

    # determines whether a grocery items's unit price is less than
    # that item's unit price
    def cheaperThan(self, that:GroceryItem) -> bool:
        return self.unitPrice() < that.unitPrice()

# implements GroceryItem
@dataclass
class Juice:
    name:str
    weight:int #grams
    price:int #cents
    flavor:str
    package:str #frozen,fresh,bottled,canned

    # computes unit price (cents per gram)
    def unitPrice(self) -> float:
        return self.price / self.weight

    #determines whether unit price is lower than a given amount
    def lowerUnitPrice(self, thatPrice) -> bool:
        return self.unitPrice() < thatPrice

    # determines whether a grocery items's unit price is less than
    # that item's unit price
    def cheaperThan(self, that:GroceryItem) -> bool:
        return self.unitPrice() < that.unitPrice()



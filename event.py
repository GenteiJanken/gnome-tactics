class EventManager:
    def __init__(self):
        self.handlers = dict()     
        self.events = []

    def register(self, event, handler):
        if not event in self.handlers:
            self.handlers[event] = []
        
        if not handler in self.handlers[event]:
            self.handlers[event].append(handler)
        return self

    def deregister(self, event, handler):       
        if not event in self.handlers:
            raise ValueError("Event is not registered")
        try:
            self.handlers[event].remove(handler)
        except:
            raise ValueError("Handler is not registered with this event.")
        return self

    def notify(self, event, *args, **kargs):   
        self.events.append((event, args, kargs))
  
    def update(self):
        for e in self.events:
            if e[0] in self.handlers:
                for h in self.handlers[e[0]]:
                    h(*e[1], **e[2]) 
        self.events = []

# Events 

# update(dt)
# Called periodically with dt set to the time in seconds it was last produced

# new_turn()
# Called when a turn is ended, causing model to update

# key_down(keyid)
# Called when a key is pressed

# key_up(keyid)
# Called when a key is released

# spell_cast(spellid, caster, flags, targets)
# When spell has been cast and the model updated, this is sent for reflection in view

# resourcechange(unit, resourceid, amount)
# Update available amount of a resource (health, mana), for reflection in view

# resourceset(unit, resourceid, amount)
# Update available amount of a resource (health, mana), for reflection in view

# spawn_entity(mapx, mapy, entity)
# queue entity spawn event

# spawned(mapx, mapy, unit, entity_type)
# Notification that an entity has been successfully constructed

# unit_kill(unit)
# Notification that a unit has been killed

# move_to(unit, mapx, mapy) 
# Attempt to move a Unit to given map coordinates

# unit_moved(unit, mapx, mapy)
# Notification that a unit has been moved to given map coordinates. 

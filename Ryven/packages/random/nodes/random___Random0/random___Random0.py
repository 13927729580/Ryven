from NENV import *


# API METHODS

# self.main_widget()        <- access to main widget
# self.update_shape()     <- recomputes the whole shape and content positions

# Ports
# self.input(index)                   <- access to input data
# self.set_output_val(index, val)    <- set output data port value
# self.exec_output(index)             <- executes an execution output

# self.create_input(type_, label, widget_name=None, widget_pos='under', pos=-1)
# self.delete_input(index or input)
# self.create_output(type_, label, pos=-1)
# self.delete_output(index or output)


# Logging
# mylog = self.new_log('Example Log')
# mylog.log('I\'m alive!!')
# self.log_message('hello global!', target='global')
# self.log_message('that\'s not good', target='error')

# ------------------------------------------------------------------------------
import random


class Random_Node(Node):
    def __init__(self, params):
        super(Random_Node, self).__init__(params)

        self.special_actions['make executable'] = {'method': self.action_make_executable}
        self.active = False

    def action_make_executable(self):
        del self.special_actions['make executable']
        self.special_actions['make passve'] = {'method': self.action_make_passive}
        self.create_input('exec', '', pos=0)
        self.create_output('exec', '', pos=0)
        self.active = True
    
    def action_make_passive(self):
        del self.special_actions['make passve']
        self.special_actions['make executable'] = {'method': self.action_make_executable}
        self.delete_input(0)
        self.delete_output(0)
        self.active = False

    def update_event(self, inp=-1):
        if self.active:
            if inp==0:
                self.set_output_val(1, random.random())
                self.exec_output(0)
        else:        
            self.set_output_val(0, random.random())
        

    def get_state(self):
        data = {'active': self.active}
        return data

    def set_state(self, data):
        self.active = data['active']

    def removing(self):
        pass

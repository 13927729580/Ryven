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


class ExtractProperty_Node(Node):
    def __init__(self, params):
        super(ExtractProperty_Node, self).__init__(params)

        self.special_actions['add param input'] = {'method': self.action_add_param_input}
        self.param_counter = 0
        self.text = ''

    def action_add_param_input(self):
        self.param_counter += 1
        self.create_input('data', 'param', widget_name=None, pos=-1)
        self.special_actions['remove param '+str(self.param_counter)] = {'method': self.action_remove_param_input, 'data': self.param_counter}

    def action_remove_param_input(self, data):
        self.delete_input(data)
        del self.special_actions['remove param '+str(self.param_counter)]
        for i in range(1, self.param_counter):
            self.special_actions['remove param '+str(i)] = {'method': self.action_remove_param_input, 'data': i}
        self.param_counter -= 1

    def update_event(self, inp=-1):
        obj = self.input(0)
        params = [self.input(i) for i in range(1, self.param_counter+1)]
        res = eval(self.text)
        self.set_output_val(0, res)

    def get_state(self):
        data = {'param counter': self.param_counter,
                'text': self.text}
        return data

    def set_state(self, data):
        self.param_counter = data['param counter']
        self.text = data['text']


    def removing(self):
        pass

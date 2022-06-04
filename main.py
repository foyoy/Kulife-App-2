import traceback
import sys
def format_exception(e):
    exception_list = traceback.format_stack()
    exception_list = exception_list[:-2]
    exception_list.extend(traceback.format_tb(sys.exc_info()[2]))
    exception_list.extend(traceback.format_exception_only(sys.exc_info()[0], sys.exc_info()[1]))
    exception_str = "Traceback (most recent call last): "
    exception_str += "".join(exception_list)
    # Removing the last \n
    exception_str = exception_str[:-1]
    return exception_str

if_error_use_this_script="""
from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
MDScreen:
    MDBoxLayout:
        padding: dp(10)
        orientation: "vertical"
        ScrollView:
            do_scroll_x: False
            do_scroll_y: True
            MDLabel:
                size_hint_y: None
                height: self.texture_size[1]
                text_size: self.width, None
                markup: True
                text: "[color=ff0000]AAAA"
'''
class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)
Test().run()
"""
try:
    exec(open("one.py").read())
except Exception as e:
    p=str("".join(traceback.format_exception(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2])))
    p2=p+str(format_exception(e))
    p2=p2.replace('"'," ").replace('\n'," ")
    exec(if_error_use_this_script.replace("AAAA",str(p2)[500:5000]))



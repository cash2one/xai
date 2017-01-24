from xai.body.inputparser import class_creation
from xai.update import add_parent
class _is():
	def __init__(self): 
		self.parents = []
		self.properties =[]
	def operate(self, obj):
		# os.path.exists('_obj1.py')
		# try:
		# 	from xai.auto_classes import obj1
		# except:
		# 	class_creation(obj1)

		add_parents([obj[0], obj[1]])
		add_childs([obj[1], obj[0]])

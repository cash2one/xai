

#calss header
class _MOOT():
	def __init__(self,): 
		self.name = "MOOT"
		self.definitions = [u'often discussed or argued about but having no definite answer: ', u'not important or not relevant, therefore not worth discussing: ', u'If a legal question is moot, it does not need to be dealt with, because something has happened that solves the issue: ', u'imagined or invented as an example, and so without any legal importance: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

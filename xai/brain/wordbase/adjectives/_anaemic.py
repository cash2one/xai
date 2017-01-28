

#calss header
class _ANAEMIC():
	def __init__(self,): 
		self.name = "ANAEMIC"
		self.definitions = [u'suffering from anaemia: ', u'without any energy and effort: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

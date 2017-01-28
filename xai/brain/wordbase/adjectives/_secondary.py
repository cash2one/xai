

#calss header
class _SECONDARY():
	def __init__(self,): 
		self.name = "SECONDARY"
		self.definitions = [u'less important than related things: ', u'developing from something similar that existed earlier: ', u'relating to the education of children approximately between the ages of 11 and 18 years old: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

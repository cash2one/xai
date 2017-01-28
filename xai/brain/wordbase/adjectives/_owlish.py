

#calss header
class _OWLISH():
	def __init__(self,): 
		self.name = "OWLISH"
		self.definitions = [u'A person who is owlish looks serious and intelligent and usually wears glasses: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _UNCOMPROMISING():
	def __init__(self,): 
		self.name = "UNCOMPROMISING"
		self.definitions = [u'If people or their beliefs are uncompromising, they are fixed and do not change, especially when faced with opposition: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

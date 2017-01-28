

#calss header
class _HUMOROUS():
	def __init__(self,): 
		self.name = "HUMOROUS"
		self.definitions = [u'funny, or making you laugh: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

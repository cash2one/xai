

#calss header
class _RESTLESS():
	def __init__(self,): 
		self.name = "RESTLESS"
		self.definitions = [u'unwilling or unable to stay still or to be quiet and calm, because you are worried or bored: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

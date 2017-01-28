

#calss header
class _SHAKEDOWN():
	def __init__(self,): 
		self.name = "SHAKEDOWN"
		self.definitions = [u'becoming organized after a period of change: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

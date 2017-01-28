

#calss header
class _SUBSONIC():
	def __init__(self,): 
		self.name = "SUBSONIC"
		self.definitions = [u'slower than the speed of sound']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

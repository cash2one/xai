

#calss header
class _SYNCOPATED():
	def __init__(self,): 
		self.name = "SYNCOPATED"
		self.definitions = [u'(of a tune) having a rhythm in which strong notes are not on the beat: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

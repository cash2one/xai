

#calss header
class _DUMB():
	def __init__(self,): 
		self.name = "DUMB"
		self.definitions = [u'permanently or temporarily unable to speak: ', u'stupid : ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

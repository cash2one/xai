

#calss header
class _HEREABOUTS():
	def __init__(self,): 
		self.name = "HEREABOUTS"
		self.definitions = [u'in this area, or near this place: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

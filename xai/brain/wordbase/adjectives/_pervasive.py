

#calss header
class _PERVASIVE():
	def __init__(self,): 
		self.name = "PERVASIVE"
		self.definitions = [u'present or noticeable in every part of a thing or place: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

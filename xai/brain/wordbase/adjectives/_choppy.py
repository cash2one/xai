

#calss header
class _CHOPPY():
	def __init__(self,): 
		self.name = "CHOPPY"
		self.definitions = [u'(of sea, lakes, or rivers) with a lot of small, rough waves caused by the wind', u'(of a hairstyle) cut at different lengths: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

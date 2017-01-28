

#calss header
class _SHOWY():
	def __init__(self,): 
		self.name = "SHOWY"
		self.definitions = [u'attracting a lot of attention by being very colourful or bright, but without any real beauty: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

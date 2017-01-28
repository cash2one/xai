

#calss header
class _TERRESTRIAL():
	def __init__(self,): 
		self.name = "TERRESTRIAL"
		self.definitions = [u'relating to the earth', u'(of a planet) similar to Earth: ', u'(of animals) living on the land rather than in the water or air', u'Terrestrial television channels are broadcast from stations on the ground and do not use satellites.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

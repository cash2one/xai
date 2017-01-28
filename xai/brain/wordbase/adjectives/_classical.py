

#calss header
class _CLASSICAL():
	def __init__(self,): 
		self.name = "CLASSICAL"
		self.definitions = [u'Classical music is considered to be part of a long, formal tradition and to be of lasting value: ', u'used to refer to a style of music written in Europe between about 1750 and 1830: ', u'traditional in style or form, or based on methods developed over a long period of time: ', u'used to describe something that is attractive because it has a simple, traditional style: ', u'belonging to or relating to the culture of ancient Rome and Greece: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

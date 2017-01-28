

#calss header
class _SAXON():
	def __init__(self,): 
		self.name = "SAXON"
		self.definitions = [u'relating to or belonging to the people who were originally from Germany and who came to live in Britain in the fifth and sixth centuries', u'belonging or relating to the German state of Saxony']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

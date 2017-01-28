

#calss header
class _MARQUEE():
	def __init__(self,): 
		self.name = "MARQUEE"
		self.definitions = [u'being the main performer or sports person in a show, film, sports event, etc. or being the performer, etc. whose name will attract most people to the show, film, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

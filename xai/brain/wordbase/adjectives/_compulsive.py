

#calss header
class _COMPULSIVE():
	def __init__(self,): 
		self.name = "COMPULSIVE"
		self.definitions = [u'doing something a lot and unable to stop doing it: ', u'If a film, play, sports event, book, etc. is compulsive, it is so interesting or exciting that you do not want to stop watching or reading it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

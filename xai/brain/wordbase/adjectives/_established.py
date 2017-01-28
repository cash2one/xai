

#calss header
class _ESTABLISHED():
	def __init__(self,): 
		self.name = "ESTABLISHED"
		self.definitions = [u'accepted or respected because of having existed for a long period of time: ', u'used for describing someone who is known for doing a job well, because they have been doing it for a long time: ', u'to start growing successfully somewhere: ', u'used for describing a Church or religion that is the official one of a country: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _INTERIOR():
	def __init__(self,): 
		self.name = "INTERIOR"
		self.definitions = [u'inside: ', u'relating to the government department in some countries that deals with subjects and events that are important in that country instead of events in other countries: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _TEMPESTUOUS():
	def __init__(self,): 
		self.name = "TEMPESTUOUS"
		self.definitions = [u'If something such as a relationship or time is tempestuous, it is full of strong emotions: ', u'of or relating to a tempest']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

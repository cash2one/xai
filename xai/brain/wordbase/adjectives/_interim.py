

#calss header
class _INTERIM():
	def __init__(self,): 
		self.name = "INTERIM"
		self.definitions = [u'temporary and intended to be used or accepted until something permanent exists: ', u"used to describe part of a company's business year, rather than the whole year: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

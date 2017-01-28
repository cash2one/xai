

#calss header
class _HON():
	def __init__(self,): 
		self.name = "HON"
		self.definitions = [u'abbreviation for  Honourable , when used as a title: ', u'abbreviation for  honorary , when used as part of a title: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

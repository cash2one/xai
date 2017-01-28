

#calss header
class _CRAZY():
	def __init__(self,): 
		self.name = "CRAZY"
		self.definitions = [u'stupid or not reasonable: ', u'mentally ill: ', u'annoyed or angry: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

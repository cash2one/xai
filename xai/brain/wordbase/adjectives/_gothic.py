

#calss header
class _GOTHIC():
	def __init__(self,): 
		self.name = "GOTHIC"
		self.definitions = [u'of or like a style of building that was common in Europe between the 12th and 16th centuries and whose characteristics are pointed arches and windows, high ceilings, and tall, thin columns: ', u'used to describe writing or films in which strange things happen in frightening places']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

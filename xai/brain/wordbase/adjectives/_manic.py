

#calss header
class _MANIC():
	def __init__(self,): 
		self.name = "MANIC"
		self.definitions = [u'very excited or anxious (= worried and nervous) in a way that causes you to be very physically active: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

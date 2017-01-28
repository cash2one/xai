

#calss header
class _CANNY():
	def __init__(self,): 
		self.name = "CANNY"
		self.definitions = [u'thinking quickly and cleverly, especially in business or financial matters: ', u'good or pleasant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

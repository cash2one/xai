

#calss header
class _LAPSED():
	def __init__(self,): 
		self.name = "LAPSED"
		self.definitions = [u'no longer involved in an activity or organization: ', u'no longer being continued or paid: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

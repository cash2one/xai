

#calss header
class _SUMMARY():
	def __init__(self,): 
		self.name = "SUMMARY"
		self.definitions = [u'done suddenly, without discussion or legal arrangements: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

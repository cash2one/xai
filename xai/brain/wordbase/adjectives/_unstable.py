

#calss header
class _UNSTABLE():
	def __init__(self,): 
		self.name = "UNSTABLE"
		self.definitions = [u'not solid and firm and therefore not strong, safe, or likely to last: ', u'An unstable person suffers from sudden and extreme changes in their mental and emotional state: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

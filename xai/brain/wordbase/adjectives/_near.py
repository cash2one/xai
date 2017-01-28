

#calss header
class _NEAR():
	def __init__(self,): 
		self.name = "NEAR"
		self.definitions = [u'not far away in distance, time, characteristics, or quality: ', u'Your near relatives are people who are closely related to you, such as your parents, brothers, or sisters.', u'at a time that is not far away: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

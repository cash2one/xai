

#calss header
class _TOKEN():
	def __init__(self,): 
		self.name = "TOKEN"
		self.definitions = [u'Token actions are done to show that you are doing something, even if the results are limited in their effect: ', u'used to refer to something that is done to prevent other people complaining, although it is not sincerely meant and has no real effect: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

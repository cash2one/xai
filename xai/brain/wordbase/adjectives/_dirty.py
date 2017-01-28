

#calss header
class _DIRTY():
	def __init__(self,): 
		self.name = "DIRTY"
		self.definitions = [u'not clean: ', u'unfair, dishonest, or unkind: ', u'used to describe something that is connected with sex, in a way that many people think is offensive: ', u'used to refer to unhealthy food such as burgers served in fashionable or expensive restaurants: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

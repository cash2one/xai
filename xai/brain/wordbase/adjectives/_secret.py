

#calss header
class _SECRET():
	def __init__(self,): 
		self.name = "SECRET"
		self.definitions = [u'If something is secret, other people are not allowed to know about it: ', u'used to refer to someone who has a particular habit, hobby, or feeling but does not tell or show other people that they do: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _CONTINUED():
	def __init__(self,): 
		self.name = "CONTINUED"
		self.definitions = [u'still happening, existing, or done: ', u'often used at the bottom of a page to show that the story, article, etc. is not finished: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

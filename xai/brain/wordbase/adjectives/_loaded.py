

#calss header
class _LOADED():
	def __init__(self,): 
		self.name = "LOADED"
		self.definitions = [u'A loaded gun has bullets in it: ', u'not fair, especially by being helpful to one person instead of another: ', u'a question that has particular words chosen to suggest the answer that is wanted: ', u'rich: ', u'drunk: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

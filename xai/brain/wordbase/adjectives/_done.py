

#calss header
class _DONE():
	def __init__(self,): 
		self.name = "DONE"
		self.definitions = [u'If something is done, or you are done with it, it is finished, or you have finished doing, using it, etc.: ', u'a plan that has been formally arranged or agreed and that is now certain to happen: ', u'cooked: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

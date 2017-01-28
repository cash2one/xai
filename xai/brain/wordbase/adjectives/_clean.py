

#calss header
class _CLEAN():
	def __init__(self,): 
		self.name = "CLEAN"
		self.definitions = [u'not dirty: ', u'honest or fair, or showing that you have not done anything illegal: ', u'not doing anything illegal, or not having or carrying illegal drugs or stolen goods: ', u'morally acceptable: ', u'not about sex: ', u'having no rough edges, and smooth, straight, or equally balanced: ', u'complete: ', u'When something you write on is clean, there is nothing on it or it is not yet used: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

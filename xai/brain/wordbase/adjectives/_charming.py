

#calss header
class _CHARMING():
	def __init__(self,): 
		self.name = "CHARMING"
		self.definitions = [u'pleasant and attractive: ', u'used to describe people who use their attractiveness to influence people or to make other people like them: ', u'used to show that you do not approve of what someone has said or done: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

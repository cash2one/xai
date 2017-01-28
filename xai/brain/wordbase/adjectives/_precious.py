

#calss header
class _PRECIOUS():
	def __init__(self,): 
		self.name = "PRECIOUS"
		self.definitions = [u'of great value because of being rare, expensive, or important: ', u'behaving in a very formal and unnatural way by giving too much attention to details that are not important and trying too hard to be perfect: ', u'used to express dislike and/or anger: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

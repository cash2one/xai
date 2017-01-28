

#calss header
class _SURE():
	def __init__(self,): 
		self.name = "SURE"
		self.definitions = [u'certain; without any doubt: ', u'certain or certainly: ', u'to be very or too confident: ', u'be confident that something is true: ', u'to have confidence in and trust someone: ', u'to be certain to: ', u'to look and/or take action to be certain that something happens, is true, etc.: ', u'If you have a sure knowledge or understanding of something, you know or understand it very well: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from users.models import Group, Profile, GroupMember


def group_manage(request, pk):

    group = Group.objects.get(id=pk)
    members = [x.group for x in GroupMember.objects.filter(group=group, status='a')]

    ctx = {
        'pk': pk,
        'group': group,
        'members': members,
    }

    return render(request, 'blog_manager/group_manage.html', ctx)


def group_info_update(request, pk):
    return HttpResponse('그룹 업데이트를 해줄 친절한 누군가를 찾아요')


def group_member_manage(request, pk):
    ctx = {
        'pk': pk,
    }
    return render(request, 'blog_manager/manage_group_member.html', ctx)


def invite_member(request, pk):
    ctx = {
        'pk': pk,
    }
    return render(request, 'blog_manager/invite_member.html', ctx)


def manage_requests(request, pk):
    group = Group.objects.get(id=pk)

    user_requests = [x.person for x in GroupMember.objects.filter(group=group, status='u')]
    group_requests = [x.person for x in GroupMember.objects.filter(group=group, status='g')]

    ctx = {
        'pk': pk,
    }

    if len(user_requests) > 0:
        ctx['user_requests'] = user_requests
        ctx['userRequest'] = True
        ctx['user_requests_count'] = len(user_requests)

    else:
        ctx['userRequest'] = False

    if len(group_requests) > 0:
        ctx['group_requests'] = group_requests
        ctx['groupRequest'] = True
        ctx['group_requests_count'] = len(group_requests)

    else:
        ctx['groupRequest'] = False

    return render(request, 'blog_manager/manage_requests.html', ctx)


# 코드가 좀 조잡하다. 좀 더 예뻤으면 좋겠다.
# 유저가 그룹에 보낸 '가입승인요청' 수용
# 새로 렌더링 하지 없게 수정하기
# 정말이냐고 알림창 띄우기
def user_request_accept(request, pk):
    if request.method == "POST":
        form = request.POST
        group = Group.objects.get(id=pk)
        group.save()

        profile_name = form.get('user_p')
        user = User.objects.get(username=profile_name)
        profile = Profile.objects.get(user=user)

        membership = GroupMember.objects.get(group=group, person=profile)

        membership.status = 'a'
        membership.save()

        return redirect('manage_requests', pk)
    return redirect('manage_requests', pk)


# 그룹이 유저에 보낸 '가입요청' 취소
# 새로고침 없게 수정하기
def group_request_cancel(request, pk):
    if request.method == "POST":
        form = request.POST
        group_id = form.get('group_id')
        group = Group.objects.get(id=group_id)
        group.save()

        profile = Profile.objects.get(user=request.user)
        membership = GroupMember.objects.get(group=group, person=profile)
        membership.delete()

        return redirect('manage_requests')
    return redirect('manage_requests')
